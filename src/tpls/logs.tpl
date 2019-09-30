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
    <a class="nav-link" href="/macs">Добавленные MAC</a>
  </li>
  <li class="nav-item">
    <a class="nav-link active" href="#">Лог</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/exit">Выход</a>
  </li>
</ul>

</div>


<div class="row">


<table class="table table-bordered table-sm" style="margin-top:40px;">

    <thead>
    <tr class="table-secondary">
         <th score="cal">Дата, время</th>
         <th score="cal">Пользователь</th>
         <th score="cal">Действие</th>
    </tr>
    </thead>

    <tbody>
          %for row in data:
          <tr>
          <td>{{row[0]}}</td>
          <td>{{row[1]}}</td>
          <td>{{row[2]}}</td>
          </tr>
          %end
    </tbody>

</table>



</div>



%include tpls/footer

