from ImplementedClass import ImplementedClass

def Implemented_instance():
	return ImplementedClass(
		visible = 'visible',
		virtual = 'virtual',
		list = [],
		read_only = 'read_only',
		not_implemented = 'not_implemented',
		is_dirty = 'True'
	)

def test_bad_init():
	try:
		ImplementedClass(
			__cache__ = {}
		)
		success = False
	except AttributeError:
		success = True
	assert success == True

def test_bad_dirty():
	a = Implemented_instance()
	try:
		a.__cache__ = {}
		success = False
	except AttributeError:
		success = True
	assert success == True

def test_init():
	a = Implemented_instance()
	assert a.visible == 'visible'
	assert a.virtual == 'virtual'
	assert a.list == []
	assert a.is_dirty == False

def test_dirty():
	a = Implemented_instance()
	assert a.is_dirty == False
	a.new_variable = None
	assert a.is_dirty == True
	a.save()
	assert a.is_dirty == False

	a.visible = 'new_visible'
	assert a.is_dirty == True
	a.save()
	a.virtual = 'new_virtual'
	assert a.is_dirty == True
	a.save()
	a.list.append(0)
	assert a.is_dirty == True
	assert a.visible == 'new_visible'
	assert a.virtual == 'new_virtual'
	assert a.list == [0]

if __name__ == '__main__':
	test_init()
	test_bad_init()
	test_dirty()
	test_bad_dirty()
