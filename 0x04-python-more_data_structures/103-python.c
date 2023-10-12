#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints list infos
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	PyObject *item;
	PyListObject *list;
	
	if (!PyList_Check(p))
	{
		printf("Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("Size of the Python List = %ld\n", PyList_Size(p));
	printf("Allocated = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints list infos
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{

	PyBytesObject *bytes = (PyBytesObject *)p;
	if (!PyBytes_Check(p))
	{
		printf("Invalid Bytes Object\n");
		return;
	}


	printf("[.] bytes object info\n");
	printf("Size of the bytes object = %ld\n", PyBytes_Size(p));
	printf("trying string: %s\n", PyUnicode_AsUTF8AndSize(p, NULL));
	printf("[*] first %ld bytes: ", PyBytes_Size(p) < 10 ? PyBytes_Size(p) : 10);

	for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; i++)
	{
		printf("%02hhx%s", bytes->ob_sval[i], i < 9 ? " " : "\n");
	}
}
