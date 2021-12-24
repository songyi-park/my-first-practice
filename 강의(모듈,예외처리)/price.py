# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price_soldier(3)

from 모듈.theater_module import *
price(4)

from 모듈.theater_module import price, price_morning

price_morning(10)

from 모듈.theater_module import price_soldier as price
price(10)
