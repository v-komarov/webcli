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
    <a class="nav-link" href="/canalfree">Общедоступные</a>
  </li>
  <li class="nav-item">
    <a class="nav-link active" href="#">Добавленные MAC</a>
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

<div class="col">
<form method='POST' action="/macs" style="margin-top:20px;margin-left:30px;">
    <dl class="row">
        <dt><label for="username">MAC</label></dt>
        <dd><input type="text" class="form-control form-control-sm" id="mac" name="mac" style="margin-left:20px;"></dd>
    </dl>
    <dl class="row">
        <dt><button type="submit" class="btn btn-outline-primary btn-sm">Добавить</button></dt>
        <dd></dd>
     </dl>
</form>
</div>


</div>


<div class="row">


<table class="table table-bordered table-sm" style="margin-top:40px;">

    <thead>
    <tr class="table-secondary">
         <th score="cal">Дата, время</th>
         <th score="cal">MAC</th>
    </tr>
    </thead>

    <tbody>
          %for row in macs:
          <tr>
          <td>{{row[1]}}</td>
          <td>{{row[0]}}</td>
          </tr>
          %end
    </tbody>

</table>



</div>






%include tpls/footer

