## Проект UI автотестов demoqa.com

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="images/logo/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>


<!-- Тест кейсы -->

### Что проверяем
* Отправка формы и проверка данных всей заполненной формы
* Отправка формы и проверка данных только с заполнением главных полей
* Отправка пустой формы и проверка валидации формы
* Поиск книги по заголовку и проверка наличия в списке
* Поиск книги по автору и проверка наличия в списке
* Поиск книги по издателю и проверка наличия в списке
* Поиск невалидной книги и отображение пустого списка 


<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/16-glebezy-python-unit14/)

##### При нажатии на "Build Now" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.
![This is an image](images/screenshots/jenkins.png)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](images/screenshots/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/allure_graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](images/screenshots/allure_suites.png)

##### Видео прохождение теста
![This is an image](images/screenshots/tests_ui.gif)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/logo/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/screenshots/tg_bot.png)
