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
        <dd><input type="text" class="form-control form-control-sm" id="mac" name="mac" style="margin-left:20px;"></dd>
    </dl>
    <dl class="row">
        <dt><button type="submit" class="btn btn-outline-primary btn-sm">Тестировать</button></dt>
        <dd></dd>
     </dl>
</form>

</div>


<div class="row col-md-7">


<table class="table table-bordered table-sm" style="margin-top:40px;">

    <thead>
    <tr class="table-secondary">
         <th score="cal">MAC</th>
         <th score="cal">IP</th>
         <th score="cal">Результат</th>
    </tr>
    </thead>

    <tbody>
          %for row in data:
          %if row['result'] == 'True':
          <tr class="text-success">
          %else:
          <tr class="text-danger">
          %end
          <td>{{row['mac']}}</td>
          <td>{{row['ip']}}</td>
          <td>{{row['result']}}</td>
          </tr>
          %end
    </tbody>

</table>



</div>




%include tpls/footer

