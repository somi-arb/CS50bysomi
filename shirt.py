import sys
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    try:
        if sys.argv[1].endswith(('.jpg', '.jpeg', '.png')):
          if sys.argv[1].split('.')[-1] == sys.argv[2].split('.')[-1]:
              input = sys.argv[1]
              output = sys.argv[2]
              tshirt_image = Image.open(input)
              person_image = Image.open('somi1.png')
              person_image = ImageOps.fit(person_image, tshirt_image.size)
              new = Image.new('RGB', tshirt_image.size)
              new.paste(tshirt_image, (0, 0))
              new.paste(person_image, (0, 0), mask=tshirt_image)
              new.save(output)
          else:
              sys.exit('input and output does not have the same extensions')
        else:
            sys.exit('file is not an Image')
    except FileExistsError:
        sys.exit('file already exists! ')
    except FileNotFoundError:
        sys.exit('file not found !')
elif len(sys.argv) < 3:
    sys.exit('too few arguments !')
elif len(sys.argv) > 3:
    sys.exit('too many arguments !')
else:
    sys.exit()