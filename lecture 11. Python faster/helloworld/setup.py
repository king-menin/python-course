#!/usr/bin/env python3
# encoding: utf-8

from distutils.core import setup, Extension

helloworld_module = Extension('helloworld_module', sources = ['helloworld/helloworld.c'])

setup(name='helloworld_module',
      version='0.1.0',
      description='Hello world module written in C',
      ext_modules=[helloworld_module])