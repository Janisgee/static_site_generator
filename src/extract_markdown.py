import re


def extract_markdown_images(text):

	matches_image = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
	return matches_image
	

	#text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

	#return a turple # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]


def extract_markdown_links(text):
	matches_link = re.findall(r"\[(.*?)\]\((.*?)\)",text)
	return matches_link

#text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

#return a turple # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

	
