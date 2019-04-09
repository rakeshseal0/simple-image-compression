import os
import sys
from PIL import Image
import yagmail

def pressMe(file, verbose=False):
	filepath = os.path.join(os.getcwd(), file)
	oldsize = os.stat(filepath).st_size
	picture = Image.open(filepath)
	dim = picture.size
	
	#set quality= to the preferred quality. 
	#I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number
	picture.save((os.getcwd()+"/Compressed/")+file,"JPEG",optimize=True,quality=40) 
	
	newsize = os.stat(os.path.join(os.getcwd()+"/Compressed/"+file)).st_size
	percent = (oldsize-newsize)/float(oldsize)*100
	if (verbose):
		print ("File compressed from {0} to {1} or {2}%".format(oldsize,newsize,percent))
	return percent



def email(dat):
	print("sending Email:")
	print(".\n.\n.")
	receiver = "am.arunava@gmail.com"
	body = "Images comprassed with % compression" + str(dat)
	content = (os.listdir(os.getcwd()+"/Compressed"))

	yag = yagmail.SMTP("sunburndk@gmail.com", "sunburndk123")



	yag.send(to=receiver,subject="Compressed Images",contents=body, attachments = content,)



def main():
	verbose = False
	#checks for verbose flag
	if (len(sys.argv)>1):
		if (sys.argv[1].lower()=="-v"):
			verbose = True

	#finds present working dir
	pwd = os.getcwd()

	tot = 0
	num = 0
	for file in os.listdir(pwd):
		if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
			num += 1
			tot += pressMe(file, verbose)
	if(tot == 0 and num == 0):
		print("No image found in directory")
		return(0)

	print ("Average Compression: %d" % (float(tot)/num))
	#email((float(tot)/num))
	print ("Done")


def huffman_traversal(root_node,tmp_array,f):		# traversal of the tree to generate codes
	if (root_node.left is not None):
		tmp_array[huffman_traversal.count] = 1
		huffman_traversal.count+=1
		huffman_traversal(root_node.left,tmp_array,f)
		huffman_traversal.count-=1
	if (root_node.right is not None):
		tmp_array[huffman_traversal.count] = 0
		huffman_traversal.count+=1
		huffman_traversal(root_node.right,tmp_array,f)
		huffman_traversal.count-=1
	else:
		huffman_traversal.output_bits[root_node.data] = huffman_traversal.count		#count the number of bits for each color
		bitstream = ''.join(str(cell) for cell in tmp_array[1:huffman_traversal.count]) 
		color = str(root_node.data)
		wr_str = color+' '+ bitstream+'\n'
		f.write(wr_str)		# write the color and the code to a file
	return


if __name__ == "__main__":
	main()