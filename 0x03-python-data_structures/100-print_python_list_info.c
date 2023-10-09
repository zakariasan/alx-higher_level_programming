#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stddef.h>
#include <string.h>
/**
 * print_python_list_info - print list infos
 * @p : python object
 *
 */
void print_python_list_info(PyObject *p)
{
	size_t i;
	PyListObject *obj;

	obj = p;
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", obj->allocated);

	i = 0;
	while (i < PyList_Size(p))
	{
		printf("Element %ld: %s\n", i,
				Py_TYPE(obj->ob_item[i])->tp_name);
		i++;
	}
}
