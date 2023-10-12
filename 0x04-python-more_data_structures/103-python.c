#include <Python.h>
#include <stddef.h>
#include <stdio.h>

/**
 * print_python_list - Prints list infos
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	PyObject *item;
	PyListObject *list;
	size_t size, i = 0;

	if (!p || !PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	size = ((PyVarObject *) p)->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	while (i < size)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		i++;
	}
}

/**
 * print_python_bytes - Prints list infos
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	size_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}


	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", size < 10 ? size : 10);

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx%s", bytes->ob_sval[i], i < 9 ? " " : "\n");
	}
}
