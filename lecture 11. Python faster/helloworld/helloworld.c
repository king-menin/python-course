#include </usr/include/python3.4m/Python.h>
#include <Python.h>

// Module method definitions
static PyObject* helloworld_module(PyObject *self, PyObject *args) {
    printf("Hello, world!\n");
    Py_RETURN_NONE;
}

static PyObject* hello(PyObject *self, PyObject *args) {
    const char* name;
    if (!PyArg_ParseTuple(args, "s", &name)) {
        return NULL;
    }

    printf("Hello, %s!\n", name);
    Py_RETURN_NONE;
}

// Method definition object for this extension, these argumens mean:
// ml_name: The name of the method
// ml_meth: Function pointer to the method implementation
// ml_flags: Flags indicating special features of this method, such as
//          accepting arguments, accepting keyword arguments, being a
//          class method, or being a static method of a class.
// ml_doc:  Contents of this method's docstring
static PyMethodDef helloworld_module_methods[] = { 
    {   
        "hello_world", helloworld_module, METH_NOARGS,
        "Print 'hello world' from a method defined in a C extension."
    },  
    {   
        "hello", hello, METH_VARARGS,
        "Print 'hello xxx' from a method defined in a C extension."
    },  
    {NULL, NULL, 0, NULL}
};

// Module definition
// The arguments of this structure tell Python what to call your extension,
// what it's methods are and where to look for it's method definitions
static struct PyModuleDef helloworld_module_definition = { 
    PyModuleDef_HEAD_INIT,
    "hello",
    "A Python module that prints 'hello world' from C code.",
    -1, 
    helloworld_module_methods
};

// Module initialization
// Python calls this function when importing your extension. It is important
// that this function is named PyInit_[[your_module_name]] exactly, and matches
// the name keyword argument in setup.py's setup() call.
PyMODINIT_FUNC PyInit_helloworld_module(void) {
    Py_Initialize();
    return PyModule_Create(&helloworld_module_definition);
}

