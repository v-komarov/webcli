%include tpls/header


<div class="row">

<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link" href="/radtest">Radtest</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/canal">Коммерческие</a>
  </li>
  <li class="nav-item">
    <a class="nav-link active" href="#">Общедоступные</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="macs">Добавленные MAC</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="log">Лог</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/exit">Выход</a>
  </li>
</ul>

</div>


<div class="row">

<div class="col">
<form method='POST' action="/canalfree" style="margin-top:20px;margin-left:30px;">
    <dl class="row">
        <dt><label for="username">IP адрес</label></dt>
        <dd><input type="text" class="form-control form-control-sm" id="ip" name="ip" style="margin-left:20px;"></dd>
    </dl>
    <dl class="row">
        <dt><button type="submit" class="btn btn-outline-primary btn-sm">Добавить</button></dt>
        <dd></dd>
     </dl>
</form>
</div>


<div class="col">
<form method='POST' action="/canalfreedel" style="margin-top:20px;margin-left:30px;">
    <dl class="row">
        <dt><label for="username">IP адрес</label></dt>
        <dd><input type="text" class="form-control form-control-sm" id="ip" name="ip" style="margin-left:20px;"></dd>
    </dl>
    <dl class="row">
        <dt><button type="submit" class="btn btn-outline-primary btn-sm">Удалить</button></dt>
        <dd></dd>
     </dl>
</form>
</div>



</div>


<ul class="list-inline">
    %for i in canals:
    <li class="list-inline-item">{{i[0]}}</li>
    %end
</ul>



%include tpls/footer

