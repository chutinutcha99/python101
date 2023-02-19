import turtle

def daisy(tao, tao_acount, tao_size):
    for i in range(tao_acount):
        for n in range(2):
            tao.forward(tao_size)
            tao.left(160)
        tao.left(360 / tao_acount)

tao = turtle.Turtle()

tao.speed("fastest")

daisy(tao, 20, 75)

turtle.done()