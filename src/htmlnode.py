class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError ("Child classes will override this")

	def props_to_html(self):
		
		new_string=""
		if self.props is None:
			return new_string
		else:
			for key,value in self.props.items():
				new_string+=f' {key}="{value}"'
			return new_string

	def __repr__(self):
		return (f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})")


class LeafNode(HTMLNode):
	def __init__(self,tag,value,props=None):
		if value is None:
			raise ValueError("All leaf nodes must have a value")
		if not props:
			props = {}
		super().__init__(tag, value, None, props)

	def to_html(self):
		if not self.value:
			raise ValueError ("All leaf nodes must have a value")

		if not self.tag:
			return self.value
		else:
			props_str = self.props_to_html()
			if props_str:
				return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
			else:
				return f'<{self.tag}>{self.value}</{self.tag}>'
	def __eq__(self, other):  # Adding this method to make comparisons valid in your tests
		return (self.tag == other.tag and self.value == other.value and self.props == other.props)


class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		if not tag:
			raise  ValueError ("All parent nodes must have a tag")
		if not children:
			raise ValueError ("All parent nodes must have a children")

		if not isinstance(children, list):
			children = [children]

		if not props:
			props = {}
		super().__init__(tag, None, children, props)

	def to_html(self):
		if not self.tag:
			raise ValueError ("All parent nodes must have a tag")
		if not self.children:
			raise ValueError ("All parent nodes must have a children")
		
		else:
			children_str = ""
			for node in self.children:
				children_str += node.to_html()
			props_str = self.props_to_html()
			if props_str:
				return f'<{self.tag} {self.props}>{children_str}</{self.tag}>'
			else:
				return f'<{self.tag}>{children_str}</{self.tag}>'





