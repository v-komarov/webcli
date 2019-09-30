%include tpls/header


<div class="row">

<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active href="#">Radtest</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/canal">Коммерческие</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/canalfree">Общедоступные</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/macs">Добавленные MAC</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/log">Лог</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/exit">Выход</a>
  </li>
</ul>

</div>


<div class="row">

<form method='POST' action="/radtest" style="margin-top:20px;margin-left:30px;">
    <dl class="row">
        <dt><label for="username">MAC адрес</label></dt>
        <dd><input type="text" class="form-control form-control-sm" id="username" name="username" style="margin-left:20px;"></dd>
    </dl>
    <dl class="row">
        <dt><button type="submit" class="btn btn-outline-primary btn-sm">Тестировать</button></dt>
        <dd></dd>
     </dl>
</form>

</div>



%include tpls/footer

