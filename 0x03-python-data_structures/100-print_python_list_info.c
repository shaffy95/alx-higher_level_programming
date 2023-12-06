#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - prints some basic info about pytohn list
* @p: python object
**/

void print_python_list_info(PyObject *p)
{
	long int size = value_of_PyList(p);
	int value;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (value = 0; value < size; value++)
		printf("Element %i: %s\n", value, Py_TYPE(obj->ob_item[value])->tp_name);
}
