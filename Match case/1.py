def describe_shape(shape):
    match shape:
        case '4 стороны': print('Квадрат')
        case '0 сторон' : print('Круг')
        case '3 стороны' : print('Треугольник')
        
describe_shape('4 стороны')
describe_shape('0 сторон')
describe_shape('3 стороны')