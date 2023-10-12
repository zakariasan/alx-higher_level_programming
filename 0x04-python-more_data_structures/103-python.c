#include <Python.h>
#include <stddef.h>
#include <stdio.h>
/**
 * print_python_bytes - Prints list infos
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	size_t size, i, max_val;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}


	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	max_val = (size >= 10) ? 10 : size + 1;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", max_val);

	for (i = 0; i < max_val; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
		 printf(" %02x", 256 + str[i]);
	}
	printf("\n");
}
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
		item = list->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		i++;
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
