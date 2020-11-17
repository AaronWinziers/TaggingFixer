import xml.etree.ElementTree as ET
import os

PATH_TO_FILES = '/home/aaron/MiMoText/Fehlersuche/ma_lueschow_programmcode/Python/erstausgaben/tagged/au/'


def join_ae_tags():
	for file in sorted(os.listdir(PATH_TO_FILES)):
		tree = ET.parse(PATH_TO_FILES + file)
		root = tree.getroot()

		for document in root:
			doc_id = document.find('entry').find('id').text
			ae_tags = document.find('entry').findall('ae')
			tag_texts = [tag.text for tag in ae_tags]
			if len(ae_tags) > 1:
				new_tag = ET.Element('ae')
				new_tag.text = ' ### '.join(tag_texts)
				for tag in ae_tags:
					document.find('entry').remove(tag)
				document.find('entry').append(new_tag)
				print("Tags combined in: " + str(doc_id))
		tree.write(PATH_TO_FILES+file, encoding='utf8', xml_declaration=False)


if __name__ == '__main__':
	join_ae_tags()
