from xmlrpc.server import SimpleXMLRPCServer
import xml.etree.ElementTree as ET
import datetime

xml = 'notebook_database.xml'
tree = ET.parse(xml)
root = tree.getroot()


def add_or_update_note(topic, text):
    global root
    timestamp = str(datetime.datetime.now())

    topic_exists = False
    for topic_element in root.findall(".//topic"):
        if topic_element.get("name") == topic:
            topic_exists = True
            note = ET.SubElement(topic_element, "note")
            ET.SubElement(note, "text").text = text
            ET.SubElement(note, "timestamp").text = timestamp
            break

    if not topic_exists:
        new_topic = ET.SubElement(root, "topic", name=topic)
        new_note = ET.SubElement(new_topic, "note")
        ET.SubElement(new_note, "text").text = text
        ET.SubElement(new_note, "timestamp").text = timestamp

    tree.write(xml)

    return "Note added or updated successfully."

def retrieve_notes(topic):
    global root
    notes = []

    for topic_element in root.findall(".//topic"):
        if topic_element.get("name") == topic:
            for note in topic_element.findall("note"):
                notes.append({
                    'text': note.find("text").text,
                    'timestamp': note.find("timestamp").text
                })

    return notes

if __name__ == '__main__':
    with SimpleXMLRPCServer(('localhost', 3333)) as server:
        server.register_introspection_functions()

        server.register_function(add_or_update_note, 'add_or_update_note')
        server.register_function(retrieve_notes, 'retrieve_notes')

        server.serve_forever()
