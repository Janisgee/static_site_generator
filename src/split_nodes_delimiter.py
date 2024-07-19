import re
from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
	
	new_list = []
	for node in old_nodes:
		if node.text_type != "text":
			new_list.append(node)
		else:
			# Split using regex
			pattern = re.escape(delimiter)
			segments=re.split(f"({pattern})",node.text)
		
			in_delimiter = False
			for segment in segments:
				if segment == delimiter:
					# toggle whether we are inside a delimiter
					in_delimiter = not in_delimiter
					continue

				if in_delimiter:
					new_list.append(TextNode(segment, text_type))
				else:
					if segment == '':
						continue
					new_list.append(TextNode(segment,"text"))

			#Check if we still have an unmatched opening delimiter
			if in_delimiter:
				raise ValueError(f"Missing closing delimiter: {delimiter}")

	return new_list
