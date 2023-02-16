from PIL import Image


class Steganography:

    def convert_pixels_to_binary(self, pixels):
        binaries = []
        for pixel in pixels:
            new_val = Steganography.convert_pixel_to_binary(self, pixel)
            binaries.append(new_val)
        return binaries

    def write_message_into_image(self, image_name):
        image = Image.open(image_name)
        if image.format == "PNG":
            pixel_values = list(image.getdata())
            pixel_values_flatten = [x for object in pixel_values for x in object]
            # print(pixel_values_flatten)
            pixels_binaries = Steganography.convert_pixels_to_binary(self, pixel_values_flatten)
            return pixels_binaries
        else:
            print("Image format must be png. Please try again.")

    # todo hide message in image
    def hide_message(self):
        return None

    # todo read message from image
    def read_message_from_image(self, image_name):
        return None

    def convert_message(self, message):
        if message.isdigt():
            return message
        else:
            # convert message to binary
            new_message = ' '.join(format(ord(character), 'b') for character in message)
            return new_message

    def convert_pixel_to_binary(self, pixel):
        return "{0:b}".format(int(pixel))


if __name__ == "__main__":
    app = Steganography()
    app.write_message_into_image("1.png")
