class search_room_begin:


def _ready():
	pass

def name():
	return 'search_room_begin'

def id():
	return 27

def length():
	return 0 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	pass