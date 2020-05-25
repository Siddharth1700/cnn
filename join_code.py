f = open("/root/attach_dir/model_train", "r")
contents = f.readlines()
f.close()

contents.insert(30, """
model.add(Conv2D(20, kernel_size=(3,3), input_shape=input_shape))
""")

f = open("/root/attach_dir/model_train", "w")
contents = "".join(contents)
f.write(contents)
f.close()