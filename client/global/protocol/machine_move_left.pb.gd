extends Node


func name():
	return 'machine_move_left'

func id():
	return 20

func length():
	return 0 ;

func send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

func parse_data( byteBuffer):
	pass
