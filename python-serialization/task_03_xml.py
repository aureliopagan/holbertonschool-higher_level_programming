#!/usr/bin/python3
"""Module for XML serialization and deserialization."""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.
    
    Args:
        dictionary: The dictionary to serialize
        filename: Path to save the XML file
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """Deserialize an XML file to a Python dictionary.
    
    Args:
        filename: Path to the XML file
        
    Returns:
        dict: The deserialized dictionary or None on error
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        return {child.tag: child.text for child in root}
        
    except (ET.ParseError, FileNotFoundError):
        return None
