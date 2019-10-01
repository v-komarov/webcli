<!doctype html>

<html lang="ru">
   <head>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

   <script src="/static/jquery-3.4.1.min.js"></script>
   <script src="/static/bootstrap-4.3.1-dist/js/bootstrap.min.js"></script>

   <link rel="stylesheet" href="/static/bootstrap-4.3.1-dist/css/bootstrap.min.css">
   
   <title>webcli</title>
   <body>

       <div class="container">

       <div class="jumbotron jumbotron-fluid">
           <div class="container">
               <h1 class="display-6">Webcli</h1>
               <p class="lead">Интерфейс управления iptv radius server</p>

               <!-- Button trigger modal -->
               <button type="button" class="btn btn-outline-success" data-toggle="modal" data-target="#ModalLong">
                  Документация
               </button>

           </div>
       </div>


<!-- Modal -->
<div class="modal fade" id="ModalLong" tabindex="-1" role="dialog" aria-labelledby="ModalLongTitle" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="ModalLongTitle">Документация</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">

      <dl class="row">
          <dt class="col-sm-3">Авторизация</dt>
          <dd class="col-sm-9">Сервис авторизации - Gamma (http://10.6.0.22:8000).
          Для доступа необходима учетная запись в Gamma.
          </dd>
          <dt class="col-sm-3">Radtest</dt>
          <dd class="col-sm-9">Тестирование radius сервера на этом сервере.
          Выбирается случайным образом два ip адреса видео каналов. Сначала общедоступный, затем коммерческий.
          Необходимо ввести mac адрес практически в любом формате.
          </dd>
      </dl>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Закрыть</button>
      </div>
    </div>
  </div>
</div>

