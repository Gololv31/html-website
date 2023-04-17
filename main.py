from flask import Flask

app = Flask(__name__)


@app.route('/Orexoff')
def main():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <link rel="stylesheet" href="style.css">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
                        rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"
                        <meta charset="utf-8">
                        <title>Интернет-магазин орехов и сухофруктов</title>
                        <style>
                        * {box-sizing: border-box;}
html, body {
    max-width: 100%;
    overflow-x: hidden;
}
form {
  position: absolute;
  width: 300px;
  margin: 0 auto;
}


.cart__num {
  position: absolute;
  background-color: #d62240;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  top: -5px;
  right: -5px;
}

input { 
  position: absolute; 
  top: 60px;
  left: 0px;
  width: 100%;
  height: 40px;
  padding-left: 10px;
  border: 2px solid #7BA7AB;
  border-radius: 5px;
  outline: none;
  background: #F9F0DA;
  color: #9E9C9C;
  font-size: 25px
}




button1 {
  position: absolute;
  top: 60px;
  left: 295px;
  font-weight: 700;
  color: white;
  text-decoration: none;
  position: absolute; 
  right: 0px;
  width: 60px;
  height: 40px;
  border: none;
  background: #7BA7AB;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
display: flex;
align-items: center;
justify-content: center
}


butt1 { 
  position: absolute;
  top: 50px;
  left: 425px;
  font-weight: 1000;
  color: white;
  text-decoration: none;
  padding: .8em 1em calc(.8em + 3px);
  background: #7BA7AB;
  border-radius: 5px;
  box-shadow: 0 -3px #7BA7AB inset;
  transition: 0.2s;
}

butt2{
position: absolute;
  top: 50px;
  left: 1100px;
  font-weight: 1000;
  color: white;
  text-decoration: none;
  padding: .8em 1em calc(.8em + 3px);
  background: #7BA7AB;
  border-radius: 5px;
  box-shadow: 0 -3px #7BA7AB inset;
  transition: 0.2s;
}

butt3{
position: absolute;
  top: 50px;
  left: 1300px;
  font-weight: 1000;
  color: white;
  text-decoration: none;
  padding: .8em 1em calc(.8em + 3px);
  background: #7BA7AB;
  border-radius: 5px;
  box-shadow: 0 -3px #7BA7AB inset;
  transition: 0.2s;
}

button:before {
  content: "\f002";
  font-family: FontAwesome;
  font-size: 16px;
  color: #F9F0DA;
}


button7 {
  position: absolute;
  left: 1525px;
  top: 0px;
  weight: 10%;
  height: 40px;
  font-weight: 1000;
  color:black;
  text-decoration: none;
  padding: .8em 1em calc(.8em + 3px);
  background: ;
  border-radius: none;
  box-shadow: none;
  transition: 0.2s;
} 

button8 {
  position: absolute;
  weight: 10%;
  height: 40px;
  font-weight: 1000;
  color:black;
  text-decoration: none;
  padding: .8em 1em calc(.8em + 3px);
  background: ;
  border-radius: none;
  box-shadow: none;
  transition: 0.2s;
} 

@import url(https://fonts.googleapis.com/css?family=Lato:400,300,100,700,900);

h1,
p,
a{
  margin: 0;
  padding: 0;
  font-family: 'Lato';
}

h1 {
  font-size: 2.8em;
  padding: 10px 0;
  font-weight: 800;
}

p {
  font-size: 1.1em;
  font-weight: 100;
  letter-spacing: 5px;
}

.header {
  position: absolute;
  left: 125px;
  top: 200px;
  width: 1450px;
  padding:60px 0;
  text-align: center;
  background: #7BA7AB;
  color: white;
}


.btn-bgstroke {
  font-size: 20px;
  display: inline-block;
  border: 1px solid white;
  padding: 10px 20px;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 300;
  margin-top: 30px; 
}

.btn-bgstroke:hover {
  background-color: white;
  color: #33cccc;
}

.card {
  width: 225px;
  min-height: 350px;
  box-shadow: 1px 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column; /* Размещаем элементы в колонку */
  border-radius: 4px;
  transition: 0.2s;
  position: relative;
}


.card:hover {
  box-shadow: 4px 8px 16px rgba(255, 102, 51, 0.2);
}

.card__top {
  flex: 0 0 220px; /* Задаем высоту 220px, запрещаем расширение и сужение по высоте */
  position: relative;
  overflow: hidden; /* Скрываем, что выходит за пределы */
}

/* Контейнер для картинки */
.card__image {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.card__image > img {
  width: 100%;
  height: 100%;
  object-fit: contain; /* Встраиваем картинку в контейнер card__image */
  transition: 0.2s;
}

/* При наведении - увеличиваем картинку */
.card__image:hover > img {
  transform: scale(1.1);
}

/* Размещаем скидку на товар относительно изображения */
.card__label {
  padding: 4px 8px;
  position: absolute;
  bottom: 10px;
  left: 10px;
  background: #ff6633;
  border-radius: 4px;
  font-weight: 400;
  font-size: 16px;
  color: #fff;
}

.card__bottom {
  display: flex;
  flex-direction: column;
  flex: 1 0 auto; /* Занимаем всю оставшуюся высоту карточки */
  padding: 10px;
}

.card__prices {
  display: flex;
  margin-bottom: 10px;
  flex: 0 0 50%; /* Размещаем цены равномерно в две колонки */
}

.card__price::after {
  content: "₽";
  margin-left: 4px;
  position: relative;
}

.card__price--discount {
  font-weight: 700;
  font-size: 19px;
  color: #414141;
  display: flex;
  flex-wrap: wrap-reverse;
}

.card__price--discount::before {
  content: "Со скидкой";
  font-weight: 400;
  font-size: 13px;
  color: #bfbfbf;
}

.card__price--common {
  font-weight: 400;
  font-size: 17px;
  color: #606060;
  display: flex;
  flex-wrap: wrap-reverse;
  justify-content: flex-end;
}

.card__price--common::before {
  content: "Обычная";
  font-weight: 400;
  font-size: 13px;
  color: #bfbfbf;
}

.card__title {
  display: block;
  margin-bottom: 10px;
  font-weight: 400;
  font-size: 17px;
  line-height: 150%;
  color: #414141;
}

.card__title:hover {
  color: #ff6633;
}

.card__add {
  display: block;
  width: 100%;
  font-weight: 400;
  font-size: 17px;
  color: #70c05b;
  padding: 10px;
  text-align: center;
  border: 1px solid #70c05b;
  border-radius: 4px;
  cursor: pointer; /* Меняем курсор при наведении */
  transition: 0.2s;
  margin-top: auto; /* Прижимаем кнопку к низу карточки */
}

.card__add:hover {
  border: 1px solid #ff6633;
  background-color: #ff6633;
  color: #fff;
}

setka {
position: absolute;
top: 600px;
left: 100px;
}

setka1 {
position: absolute;
top: 1200px;

}

html, body {
    max-width: 100%;
    overflow-x: hidden;
}

table.tb1{
left: 120px;
position: absolute;
top: 675px;
border-spacing: 10px 10px;
}

table.tb2{
left: 120px;
position: absolute;
top: 1750px;
border-spacing: 10px 10px;
}

h1.vir{
position: absolute;
top: 550px;
left: 750px;
}
h1.vir2{
position: absolute;
top: 1600px;
left: 700px;
}




                        </style>

                      </head>
                      <body>
               

   <div class="container">
     <div class="row">
       <div class="col-4">

         <a href=Orexoff><img src=static/img/orexoff.png width="200" height="105"></a>
       </div>
      
       <div class="col">
         <form>
         <input type="text" placeholder="Искать здесь...">
         <button1 type="submit">Поиск</button>
         </form>
       </div>
       <div class="col">
         <butt2 type="button" onclick="document.location='Orexoff/korzina'">Корзина <img src="static/img/корзина.png" weight="20" height="20">
         <div class="cart__num" id="cart_num">0</div></button>
       </div>
       <div class="col">
         <butt3 type="button" onclick="document.location='Orexoff/login'">Вход/Регистрация <img src="static/img/пользователь.png" weight="20" height="20"></button>
       </div>
       <div class="col">
         <button7 type="button">Отзыв <img src="static/img/отзыв.png" weight="20" height="20"></button>
       </div>


       <section class="header">
    <h1>Весенняя акция</h1>
    <p>Скидка на все товары 10%</p>
    <a class="btn-bgstroke">Посмотреть</a>
     </section>

<h1 class="vir">Орехи</h1>

<table class="tb1">
  <tr>
    <td>
<div class="card">
  <div class="card__top">
    <a href="/Orexoff/araxis" class="card__image">
      <img
        src="/static/img/арахис.jpg"
        alt="Арахис 200гр."
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">198.75</div>
      <div class="card__price card__price--common">218.99</div>
    </div>
    <a href="/Orexoff/araxis" class="card__title">
      Арахис жареный соленый, 500 г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
<td>
<div class="card">
  <div class="card__top">
    <a href="/Orexoff/gretski" class="card__image">
      <img
        src="static/img/грецкий орех.jpg"
        alt="Грецкий орех очищенный без обжарки, 500 г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">311.50</div>
      <div class="card__price card__price--common">345.75</div>
    </div>
    <a href="/Orexoff/gretski" class="card__title">
      Грецкий орех в скорлупе, 500 г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
    <td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/кешью.jpg"
        alt="Кешью сырой сушеный, 500 г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">374.65</div>
      <div class="card__price card__price--common">415.95</div>
    </div>
    <a href="#" class="card__title">
      Кешью сырой сушеный, 500 г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
<td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/миндаль.jpg"
        alt="Миндаль сырой очищенный орехи 500г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">464.99</div>
      <div class="card__price card__price--common">515.69</div>
    </div>
    <a href="#" class="card__title">
      Миндаль сырой очищенный орехи, 500г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
  </tr>
  <tr>
  <td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/бразильский.jpg"
        alt="Бразильский орех очищенный 500 г."
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">456.00</div>
      <div class="card__price card__price--common">507.00</div>
    </div>
    <a href="#" class="card__title">
      Бразильский орех очищенный, 500 г.
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
   <td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/фисташки.jpg"
        alt="Фисташки жареные солёные 500г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">574.99</div>
      <div class="card__price card__price--common">637.59</div>
    </div>
    <a href="#" class="card__title">
      Фисташки жареные солёные, 500г
    </a>
    <!-- Кнопка добавить в корзину -->
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
    <td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/фундук.jpg"
        alt="Фундук сырой сушеный, 500г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">384.65</div>
      <div class="card__price card__price--common">427.75</div>
    </div>
    <a href="#" class="card__title">
      Фундук сырой сушеный, 500г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
<td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/пекан.jpeg"
        alt="Пекан в скорлупе, 500 г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">645.76</div>
      <div class="card__price card__price--common">709.95</div>
    </div>
    <a href="#" class="card__title">
     Пекан очищенный сырой, 500 гр
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
  </tr>
</table>


<h1 class="vir2">Сухофрукты</h1> 









<table class="tb2">
  <tr>
    <td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="/static/img/вишня.jpg"
        alt="Вишня сушеная вяленая, 150 г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">302.96</div>
      <div class="card__price card__price--common">337.55</div>
    </div>
    <a href="#" class="card__title">
      Вишня сушеная вяленая, 150 г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
<td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/изюм.jpg"
        alt="Изюм темный сушеный, 150 г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">90.65</div>
      <div class="card__price card__price--common">101.95</div>
    </div>
    <a href="#" class="card__title">
      Изюм темный сушеный, 150 г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
    <td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/инжир.jpg"
        alt="Инжир отборный сушеный, 150 г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">172.50</div>
      <div class="card__price card__price--common">198.90</div>
    </div>
    <a href="#" class="card__title">
      Инжир отборный сушеный, 150 г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
<td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/курага.jpg"
        alt="Курага сушенная без косточки, 150 г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">141.85</div>
      <div class="card__price card__price--common">163.97</div>
    </div>
    <a href="#" class="card__title">
      Курага сушенная без косточки, 150 г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
  </tr>
  <tr>
  <td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/финики.jpg"
        alt="Сушенные финики с косточкой, 150г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">129.78</div>
      <div class="card__price card__price--common">142.99</div>
    </div>
    <a href="#" class="card__title">
      Сушенные финики с косточкой, 150г.
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
   <td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/чернослив.jpg"
        alt="Чернослив сушеный без косточки, 150 г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">128.99</div>
      <div class="card__price card__price--common">154.87</div>
    </div>
    <a href="#" class="card__title">
      Чернослив сушеный без косточки, 150 г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
    <td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/цукаты.jpg"
        alt="Цукаты ананаса кубики микс, 150г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">298.99</div>
      <div class="card__price card__price--common">329.55</div>
    </div>
    <a href="#" class="card__title">
      Цукаты ананаса кубики микс, 150г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
<td>
<div class="card">
  <div class="card__top">
    <a href="#" class="card__image">
      <img
        src="static/img/папайя.jpg"
        alt="Сушенная папайя ломтики, 150г"
      />
    </a>
    <div class="card__label">-10%</div>
  </div>
  <div class="card__bottom">
    <div class="card__prices">
      <div class="card__price card__price--discount">202.85</div>
      <div class="card__price card__price--common">224.55</div>
    </div>
    <a href="#" class="card__title">
    Сушенная папайя ломтики, 150г
    </a>
    <button class="card__add">В корзину</button>
  </div>
</div>
</td>
  </tr>
</table>


        </body>
                    </html>"""

@app.route('/Orexoff/login')
def Login():
    return """<!doctype html>
                <html lang="en">
                  <head>
                  <link rel="stylesheet" type="text/css" href="style.css" />
                  <link rel="stylesheet" type="text/css" href="slide navbar style.css">
                <link href="https://fonts.googleapis.com/css2?family=Jost:wght@500&display=swap" rel="stylesheet">
                    <meta charset="utf-8">
                    <title>Регистрация</title>
                    <style>
body{
	margin: 0;
	padding: 0;
	display: flex;
	justify-content: center;
	align-items: center;
	min-height: 100vh;
	font-family: 'Jost', sans-serif;
	background: white;
}
.main{
	width: 350px;
	height: 500px;
	background: red;
	overflow: hidden;
    background: #7BA7AB;
	border-radius: 10px;
	box-shadow: 5px 20px 50px #000;
}
#chk{
	display: none;
}
.signup{
	position: relative;
	width:100%;
	height: 100%;
}
label{
	color: white;
	font-size: 2.3em;
	justify-content: center;
	display: flex;
	margin: 60px;
	font-weight: bold;
	cursor: pointer;
	transition: .5s ease-in-out;
}
input{
	width: 60%;
	height: 20px;
	background: #e0dede;
	justify-content: center;
	display: flex;
	margin: 20px auto;
	padding: 10px;
	border: none;
	outline: none;
	border-radius: 5px;
}
button{
	width: 60%;
	height: 40px;
	margin: 10px auto;
	justify-content: center;
	display: block;
	color: #fff;
	background: #7BA7AB;
	font-size: 1em;
	font-weight: bold;
	margin-top: 20px;
	outline: none;
	border: none;
	border-radius: 5px;
	transition: .2s ease-in;
	cursor: pointer;
}


button:hover{
	background: #7BA7AB;
}

.login{
	height: 460px;
	background: #eee;
	border-radius: 60% / 10%;
	transform: translateY(-180px);
	transition: .8s ease-in-out;
}
.login label{
	color: #7BA7AB;
	transform: scale(.6);
}

#chk:checked ~ .login{
	transform: translateY(-500px);
}
#chk:checked ~ .login label{
	transform: scale(1);	
}
#chk:checked ~ .signup label{
	transform: scale(.6);
}

a{
position: absolute;
top: 10px;
left: 175px;
}

butt3 { 
  position: absolute;
  top: 10px;
  left: 125px;
  font-weight: 1000;
  color: white;
  text-decoration: none;
  padding: .8em 1em calc(.8em + 3px);
  background: #7BA7AB;
  border-radius: 5px;
  box-shadow: 0 -3px #7BA7AB inset;
  transition: 0.2s;
}


                    </style>
                    
                  </head>
                  <body>
 
                  
<div class="main">  	
		<input type="checkbox" id="chk" aria-hidden="true">
			<div class="signup">
				<form>
					<label for="chk" aria-hidden="true">Регистрация</label>
					<input type="text" name="txt" placeholder="Имя" required="">
					<input type="email" name="email" placeholder="Адрес почты" required="">
					<input type="password" name="pswd" placeholder="Пароль" required="">
					<button>Регистрация</button>
				</form>
			</div>

			<div class="login">
				<form>
					<label for="chk" aria-hidden="true">Вход</label>
					<input type="email" name="email" placeholder="Адрес почты" required="">
					<input type="password" name="pswd" placeholder="Пароль" required="">
					<button>Вход</button>
				</form>
			</div>
	</div>
	
	<butt3 type="button" onclick="document.location='http://127.0.0.1:8080/Orexoff'"> На главную</button> 
	
                  </body>
                </html>"""

@app.route('/Orexoff/korzina')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Корзина</title>
                    <style>
                    * {
  box-sizing: border-box;
}
 
 
butt3 { 
  position: absolute;
  top: 10px;
  left: 125px;
  font-weight: 1000;
  color: #7BA7AB;
  text-decoration: none;
  padding: .8em 1em calc(.8em + 3px);
  background: white;
  border-radius: 5px;
  box-shadow: 0 -3px #7BA7AB inset;
  transition: 0.2s;
}

html,
body {
  width: 100%;
  height: 100%;
  margin: 0;
  background-color: #7BA7AB;
  font-family: 'Roboto', sans-serif;
}

.shopping-cart {
  width: 750px;
  height: 423px;
  margin: 80px auto;
  background: #FFFFFF;
  box-shadow: 1px 2px 3px 0px rgba(0,0,0,0.10);
  border-radius: 6px;
 
  display: flex;
  flex-direction: column;
}

.title {
  height: 60px;
  border-bottom: 1px solid #E1E8EE;
  padding: 20px 30px;
  color: #5E6977;
  font-size: 18px;
  font-weight: 400;
}
 
.item {
  padding: 20px 30px;
  height: 120px;
  display: flex;
}
 
.item:nth-child(3) {
  border-top:  1px solid #E1E8EE;
  border-bottom:  1px solid #E1E8EE;
}

.buttons {
  position: relative;
  padding-top: 30px;
  margin-right: 60px;
}
.delete-btn,
.like-btn {
  display: inline-block;
  Cursor: pointer;
}
.delete-btn {
  width: 18px;
  height: 17px;
  background: url("delete-icn.svg") no-repeat center;
}
 
.like-btn {
  position: absolute;
  top: 9px;
  left: 15px;
  background: url('twitter-heart.png');
  width: 60px;
  height: 60px;
  background-size: 2900%;
  background-repeat: no-repeat;
}

.is-active {
  animation-name: animate;
  animation-duration: .8s;
  animation-iteration-count: 1;
  animation-timing-function: steps(28);
  animation-fill-mode: forwards;
}
 
@keyframes animate {
  0%   { background-position: left;  }
  50%  { background-position: right; }
  100% { background-position: right; }
}

.image {
  margin-right: 50px;
}
 
Let’s add some basic style to  product name and description.
.description {
  padding-top: 10px;
  margin-right: 60px;
  width: 115px;
}
 
.description span {
  display: block;
  font-size: 14px;
  color: #43484D;
  font-weight: 400;
}
 
.description span:first-child {
  margin-bottom: 5px;
}
.description span:last-child {
  font-weight: 300;
  margin-top: 8px;
  color: #86939E;
}

.quantity {
  padding-top: 20px;
  margin-right: 60px;
}
.quantity input {
  -webkit-appearance: none;
  border: none;
  text-align: center;
  width: 32px;
  font-size: 16px;
  color: #43484D;
  font-weight: 300;
}
 
button[class*=btn] {
  width: 30px;
  height: 30px;
  background-color: #E1E8EE;
  border-radius: 6px;
  border: none;
  cursor: pointer;
}
.minus-btn img {
  margin-bottom: 3px;
}
.plus-btn img {
  margin-top: 2px;
}
 
button:focus,
input:focus {
  outline:0;
}

.total-price {
  width: 83px;
  padding-top: 27px;
  text-align: center;
  font-size: 16px;
  color: #43484D;
  font-weight: 300;
}

@media (max-width: 800px) {
  .shopping-cart {
    width: 100%;
    height: auto;
    overflow: hidden;
  }
  .item {
    height: auto;
    flex-wrap: wrap;
    justify-content: center;
  }
  .image img {
    width: 50%;
  }
  .image,
  .quantity,
  .description {
    width: 100%;
    text-align: center;
    margin: 6px 0;
  }
  .buttons {
    margin-right: 20px;
  }
}


                    </style>
                  </head>
                  <body>
                  <div class="shopping-cart">
      <!-- Title -->
      <div class="title">
        Корзина
      </div>
 
      <!-- Товар #1 -->
      <div class="item">
        <div class="buttons">
          <span class="delete-btn"></span>
          <span class="like-btn"></span>
        </div>
 
        <div class="image">
          <img src="item-1.png" alt="" />
        </div>
 
        <div class="description">
          <span>Common Projects</span>
          <span>Bball High</span>
          <span>White</span>
        </div>
 
        <div class="quantity">
          <button class="plus-btn" type="button" name="button">
            <img src="static/img/плюс.png" height="20">
          </button>
          <input type="text" name="name" value="1">
          <button class="minus-btn" type="button" name="button">
           <img src="static/img/минус.png" height="20">
          </button>
        </div>
 
        <div class="total-price">$549</div>
      </div>
 
      <!-- Товар #2 -->
      <div class="item">
        <div class="buttons">
          <span class="delete-btn"></span>
          <span class="like-btn"></span>
        </div>
 
        <div class="image">
          <img src="item-2.png" alt=""/>
        </div>
 
        <div class="description">
          <span>Maison Margiela</span>
          <span>Future Sneakers</span>
          <span>White</span>
        </div>
 
        <div class="quantity">
          <button class="plus-btn" type="button" name="button">
            <img src="static/img/плюс.png" height="20">
          </button>
          <input type="text" name="name" value="1">
          <button class="minus-btn" type="button" name="button">
            <img src="static/img/минус.png" height="20">
          </button>
        </div>
 
        <div class="total-price">$870</div>
      </div>
 
      <!-- Товар #3 -->
      <div class="item">
        <div class="buttons">
          <span class="delete-btn"></span>
          <span class="like-btn"></span>
        </div>
 
        <div class="image">
          <img src="item-3.png" alt="" />
        </div>
 
        <div class="description">
          <span>Our Legacy</span>
          <span>Brushed Scarf</span>
          <span>Brown</span>
        </div>
 
        <div class="quantity">
          <button class="plus-btn" type="button" name="button">
           <img src="static/img/плюс.png" height="20">
          </button>
          <input type="text" name="name" value="1">
          <button class="minus-btn" type="button" name="button">
            <img src="static/img/минус.png" height="20">
          </button>
        </div>
 
        <div class="total-price">$349</div>
      </div>
    </div>
    
<butt3 type="button" onclick="document.location='http://127.0.0.1:8080/Orexoff'"> На главную</button>
                  </body>
                </html>"""


@app.route('/Orexoff/araxis')
def araxis():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <style>/* ----- Variables ----- */

$color-primary: #4c4c4c;
$color-secondary: #a6a6a6;
$color-highlight: #ff3f40;

/* ----- Global ----- */
* {
  box-sizing: border-box;
}

html,
body {
  height: 100%;
}

body {
  display: grid;
  grid-template-rows: 1fr;
  font-family: "Raleway", sans-serif;
  background-color: #7BA7AB;
}

h3 {
  font-size: 0.7em;
  letter-spacing: 1.2px;
  color: $color-secondary;
}

img {
      max-width: 100%;
      filter: drop-shadow(1px 1px 3px $color-secondary);
    }

/* ----- Product Section ----- */
.product {
  display: grid;
  grid-template-columns: 0.9fr 1fr;
  margin: auto;
  padding: 2.5em 0;
  min-width: 600px;
  background-color: white;
  border-radius: 5px;
}

/* ----- Photo Section ----- */
.product__photo {
  position: relative;
}

.photo-container {
  position: absolute;
  left: -2.5em;
  display: grid;
  grid-template-rows: 1fr;
  width: 100%;
  height: 100%;
  border-radius: 6px;
  box-shadow: 4px 4px 25px -2px rgba(0, 0, 0, 0.3);
}

.photo-main {
  border-radius: 6px 6px 0 0;
  background-color: white;
  background: "white";

  .controls {
    display: flex;
    justify-content: space-between;
    padding: 0.8em;
    color: #fff;

    i {
      cursor: pointer;
    }
  }

  img {
    position: absolute;
    left: -3.5em;
    top: 2em;
    max-width: 110%;
    filter: saturate(150%) contrast(120%) hue-rotate(10deg)
      drop-shadow(1px 20px 10px rgba(0, 0, 0, 0.3));
  }
}

.photo-album {
  padding: 0.7em 1em;
  border-radius: 0 0 6px 6px;
  background-color: #fff;

  ul {
    display: flex;
    justify-content: space-around;
  }

  li {
    float: left;
    width: 55px;
    height: 55px;
    padding: 7px;
    border: 1px solid $color-secondary;
    border-radius: 3px;
  }
}

/* ----- Informations Section ----- */
.product__info {
  padding: 0.8em 0;
}

.title {
  h1 {
    margin-bottom: 0.1em;
    color: $color-primary;
    font-size: 1.5em;
    font-weight: 900;
  }

  span {
    font-size: 0.7em;
    color: $color-secondary;
  }
}

.price {
  margin: 1.5em 0;
  color: $color-highlight;
  font-size: 1.2em;

  span {
    padding-left: 0.15em;
    font-size: 2.9em;
  }
}

.variant {
  overflow: auto;

  h3 {
    margin-bottom: 1.1em;
  }

  li {
    float: left;
    width: 35px;
    height: 35px;
    padding: 3px;
    border: 1px solid transparent;
    border-radius: 3px;
    cursor: pointer;

    &:first-child,
    &:hover {
      border: 1px solid $color-secondary;
    }
  }

  li:not(:first-child) {
    margin-left: 0.1em;
  }
}

.description {
  clear: left;
  margin: 2em 0;

  h3 {
    margin-bottom: 1em;
  }

  ul {
    font-size: 0.8em;
    list-style: disc;
    margin-left: 1em;
  }

  li {
    text-indent: -0.6em;
    margin-bottom: 0.5em;
  }
}

.buy--btn {
  padding: 1.5em 3.1em;
  border: none;
  border-radius: 7px;
  font-size: 0.8em;
  font-weight: 700;
  letter-spacing: 1.3px;
  color: #fff;
  background-color: #ff3f40;
  box-shadow: 2px 2px 25px -7px $color-primary;
  cursor: pointer;

  &:active {
    transform: scale(0.97);
  }
}

/* ----- Footer Section ----- */
footer {
  padding: 1em;
  text-align: center;
  color: #fff;

  a {
    color: $color-primary;

    &:hover {
      color: $color-highlight;
    }
  }
}
                    </style>
                  </head>
                  <body>
                    <section class="product">
  <div class="product__photo">
    <div class="photo-container">
      <div class="photo-main">
        
        <img src="static/img/арахис.jpg">
      </div>
      
    </div>
  </div>
  <div class="product__info">
    <div class="title">
      <h1>Арахис жаренный</h1>
      <span>500 Г</span>
    </div>
    <div class="price">
      ₽<span>198.75</span>
    </div>
    
    <div class="description">
      <h3>ПОЛЬЗА</h3>
      <ul>
        <li>Витамин E</li>
        <li>Витамин РР</li>
        <li>Витамин B</li>
        <li>Полезно для сердечно-сосудистой системы</li>
      </ul>
    </div>
    <button class="buy--btn">В КОРЗИНУ</button>
  </div>
</section>

<footer>
  <p>Design from <a href="https://dribbble.com/shots/5216438-Daily-UI-012">dribbble shot</a> of <a href="https://dribbble.com/rodrigorramos">Rodrigo Ramos</a></p>
</footer>
                  </body>
                </html>"""


@app.route('/Orexoff/gretski')
def gretski():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <style>
                    
$color-primary: #4c4c4c;
$color-secondary: #a6a6a6;
$color-highlight: #ff3f40;

/* ----- Global ----- */
* {
  box-sizing: border-box;
}

html,
body {
  height: 100%;
}

body {
  display: grid;
  grid-template-rows: 1fr;
  font-family: "Raleway", sans-serif;
  background-color: #7BA7AB;
}

h3 {
  font-size: 0.7em;
  letter-spacing: 1.2px;
  color: $color-secondary;
}

img {
      max-width: 100%;
      filter: drop-shadow(1px 1px 3px $color-secondary);
    }

/* ----- Product Section ----- */
.product {
  display: grid;
  grid-template-columns: 0.9fr 1fr;
  margin: auto;
  padding: 2.5em 0;
  min-width: 600px;
  background-color: white;
  border-radius: 5px;
}

/* ----- Photo Section ----- */
.product__photo {
  position: relative;
}

.photo-container {
  position: absolute;
  left: -2.5em;
  display: grid;
  grid-template-rows: 1fr;
  width: 100%;
  height: 100%;
  border-radius: 6px;
  box-shadow: 4px 4px 25px -2px rgba(0, 0, 0, 0.3);
}

.photo-main {
  border-radius: 6px 6px 0 0;
  background-color: white;
  background: "white";

  .controls {
    display: flex;
    justify-content: space-between;
    padding: 0.8em;
    color: #fff;

    i {
      cursor: pointer;
    }
  }

  img {
    position: absolute;
    left: -3.5em;
    top: 2em;
    max-width: 110%;
    filter: saturate(150%) contrast(120%) hue-rotate(10deg)
      drop-shadow(1px 20px 10px rgba(0, 0, 0, 0.3));
  }
}

.photo-album {
  padding: 0.7em 1em;
  border-radius: 0 0 6px 6px;
  background-color: #fff;

  ul {
    display: flex;
    justify-content: space-around;
  }

  li {
    float: left;
    width: 55px;
    height: 55px;
    padding: 7px;
    border: 1px solid $color-secondary;
    border-radius: 3px;
  }
}

/* ----- Informations Section ----- */
.product__info {
  padding: 0.8em 0;
}

.title {
  h1 {
    margin-bottom: 0.1em;
    color: $color-primary;
    font-size: 1.5em;
    font-weight: 900;
  }

  span {
    font-size: 0.7em;
    color: $color-secondary;
  }
}

.price {
  margin: 1.5em 0;
  color: $color-highlight;
  font-size: 1.2em;

  span {
    padding-left: 0.15em;
    font-size: 2.9em;
  }
}

.variant {
  overflow: auto;

  h3 {
    margin-bottom: 1.1em;
  }

  li {
    float: left;
    width: 35px;
    height: 35px;
    padding: 3px;
    border: 1px solid transparent;
    border-radius: 3px;
    cursor: pointer;

    &:first-child,
    &:hover {
      border: 1px solid $color-secondary;
    }
  }

  li:not(:first-child) {
    margin-left: 0.1em;
  }
}

.description {
  clear: left;
  margin: 2em 0;

  h3 {
    margin-bottom: 1em;
  }

  ul {
    font-size: 0.8em;
    list-style: disc;
    margin-left: 1em;
  }

  li {
    text-indent: -0.6em;
    margin-bottom: 0.5em;
  }
}

.buy--btn {
  padding: 1.5em 3.1em;
  border: none;
  border-radius: 7px;
  font-size: 0.8em;
  font-weight: 700;
  letter-spacing: 1.3px;
  color: #fff;
  background-color: #ff3f40;
  box-shadow: 2px 2px 25px -7px $color-primary;
  cursor: pointer;

  &:active {
    transform: scale(0.97);
  }
}

/* ----- Footer Section ----- */
footer {
  padding: 1em;
  text-align: center;
  color: #fff;

  a {
    color: $color-primary;

    &:hover {
      color: $color-highlight;
    }
  }
}
                    </style>
                  </head>
                  <body>
                     <section class="product">
  <div class="product__photo">
    <div class="photo-container">
      <div class="photo-main">
        
        <img src="static/img/арахис.jpg">
      </div>
      
    </div>
  </div>
  <div class="product__info">
    <div class="title">
      <h1>Арахис жаренный</h1>
      <span>500 Г</span>
    </div>
    <div class="price">
      ₽<span>198.75</span>
    </div>
    
    <div class="description">
      <h3>ПОЛЬЗА</h3>
      <ul>
        <li>Витамин E</li>
        <li>Витамин РР</li>
        <li>Витамин B</li>
        <li>Полезно для сердечно-сосудистой системы</li>
      </ul>
    </div>
    <button class="buy--btn">В КОРЗИНУ</button>
  </div>
</section>

<footer>
  <p>Design from <a href="https://dribbble.com/shots/5216438-Daily-UI-012">dribbble shot</a> of <a href="https://dribbble.com/rodrigorramos">Rodrigo Ramos</a></p>
</footer>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
