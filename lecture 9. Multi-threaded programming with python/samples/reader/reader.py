# -*- coding: utf-8 -*-
import subprocess as sp
from .search_text import search_text as st
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
from .search_text import thread_job_multi_proc

class WikiReader(object):

    @property
    def queries(self):
        return self.__queries

    @property
    def template(self):
        return self.__tmp

    def __init__(self, queries=list(), search_text=st):
        self.__queries = queries
        self.__tmp = "https://en.wikipedia.org/w/index.php?{}"
        self.search_text = search_text

    def add_query(self, query):
        self.__queries.append(query)

    def run_synchronously(self):
        return dict(zip(self.__queries, map(self.search_text,
                                            zip([self.__tmp] * len(self.__queries), self.__queries))))

    def run_async_sub_proc(self):
        def communicate(sub_process):
            out, _ = sub_process.communicate()
            return out.decode("utf-8").split("\n")

        sub_processes = [
            sp.Popen(["python", "./reader/search_text.py", self.__tmp, query],
                     stdout=sp.PIPE, stderr=sp.PIPE)
            for query in self.__queries]
        res = []
        for sub_process, query in zip(sub_processes, self.__queries):
            res.append(communicate(sub_process))
        if not all(map(lambda x: x[0][0].strip() == x[1], zip(res, self.__queries))):
            print("Failed on results order")
        return dict(zip(self.__queries, list(map(lambda x: x[1], res))))

    def run_async_thread(self):
        res = list()

        def thread_job(tmp, query):
            res.append((query, self.search_text((tmp, query))))

        threads = [threading.Thread(target=thread_job, args=(self.__tmp, query,))
                   for query in self.__queries]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        if not all(map(lambda x: x[0][0].strip() == x[1], zip(res, self.__queries))):
            print("Failed on results order")

        return dict(res)

    def run_async_thread_with_q(self):
        def thread_job(input_q, output_q):
            while True:
                tmp, query = input_q.get()
                res = (query, self.search_text((tmp, query)))
                output_q.put(res)
                input_q.task_done()

        def data_generator(input_q, tmp, query):
            input_q.put((tmp, query))

        input_q = Queue()
        output_q = Queue()

        thread_job_daemon = threading.Thread(target=thread_job,
                             args=(input_q, output_q), daemon=True)
        thread_job_daemon.start()

        threads = [threading.Thread(target=data_generator, args=(input_q, self.__tmp, query, ))
                   for query in self.__queries]
        for thread in threads:
            thread.start()
        res = []
        for thread, query in zip(threads, self.__queries):
            res.append(output_q.get())
            thread.join()
        if not all(map(lambda x: x[0][0].strip() == x[1], zip(res, self.__queries))):
            print("Failed on results order")
        input_q.join()
        return dict(res)

    def run_async_multiprocess(self):
        with multiprocessing.Pool(8) as executor:
            res = list(executor.map(thread_job_multi_proc,
                                    zip([self.__tmp] * len(self.__queries), self.__queries)))
        if not all(map(lambda x: x[0][0].strip() == x[1], zip(res, self.__queries))):
            print("Failed on results order")
        return dict(res)
    pass
