from PIL import Image
import easyocr
import os


NAME_IMG = ['image_par_1.jpg', 'image_par_2.jpg', 'image_par_3.jpg']


def split_image(file_path, name_img):
    img = Image.open(file_path)
    width, height = img.size
    part_height = int(height / 3)
    part_height_2 = part_height * 2
    img_part_1 = img.crop((0, 0, width, part_height))
    img_part_2 = img.crop((0, part_height, width, part_height_2))
    img_part_3 = img.crop((0, part_height_2, width, height))
    img_part_1.save(name_img[0])
    img_part_2.save(name_img[1])
    img_part_3.save(name_img[2])


def data_recognition(file):
    reader = easyocr.Reader(["de"], verbose=False)
    result = reader.readtext(file, detail=0)
    return result


def delete_img_part():
    for i in NAME_IMG:
        os.remove(i)


def recognition_img(file_path):
    split_image(file_path, NAME_IMG)
    result = []
    for i in NAME_IMG:
        data_recognized = data_recognition(i)
        result.append(data_recognized[0].lower().replace('i', 'l').split('l'))
    return result

    delete_img_part()


if __name__ == '__main__':
    recognition_img()



