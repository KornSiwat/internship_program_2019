import xml.etree.ElementTree as et
import json

def start():
    '''
    this function ask for the xml file name then convert and create an json file of the input
    '''
    finName = input("Enter XML File Name: ")
    name = finName.replace('.xml', '')
    tree = et.parse(finName)
    root = tree.getroot()
    xml_dict = xml_to_dict(root)
    dict_to_json_file(xml_dict, name)

def xml_to_dict(xml_root):
    ''' 
    this function take the root element of xml.etree.ElementTree.Element to convert and return in dictionary type
    '''
    is_et_element(xml_root)
    result = dict()
    for node in xml_root:
        result.update(node_to_dict(node))
    return result

def node_to_dict(node):
    ''' 
    this function is a recursive function that take node (type of xml.etree.ElementTree.Element) which recurse and
    create dictionary containg details of next level nodes until it reaches a leaf node.
    '''
    is_et_element(node)
    result = dict()
    if len(node) == 0:
        result[node.tag] = return_attrib_text(node)
        return result
    else:
        result[node.tag] =  return_attrib_text(node)
        for child in node:

            result[node.tag].update(node_to_dict(child))
        return result

def return_attrib_text(node):
    ''' 
    this function take element in type of xml.etree.ElementTree.Element and return dictonary containing its attribute or text or both if exist
    '''
    is_et_element(node)
    result = dict()
    if node.text != None:
        node.text = node.text.strip()
    if len(node.attrib) != 0 and node.text != '' and node.text != None:
        for key in node.attrib:
            result[key] = node.attrib[key]
        result['text'] = node.text
    elif len(node.attrib) >= 1:
        for key in node.attrib:
            result[key] = node.attrib[key]
    elif len(node.attrib) == 0 and node.text != '':
        result = node.text
    return result

def dict_to_json_file(xml_dict, out_name):
    with open(f'{out_name}.json', 'w') as output:
        json.dump(xml_dict, output)

def is_et_element(data):
    '''
    function to check if type is xml.etree.ElementTree.Element
    '''
    if isinstance(data , et.Element):
        return True
    else:
        raise TypeError("Input is not xml.etree.ElementTree.Element")

if __name__ == "__main__":
    start()