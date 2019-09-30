%include tpls/header


<div class="row justify-content-center">

<form method='POST'>
  <div class="form-group row small">
    <label for="username">Пользователь</label>
    <input type="text" class="form-control form-control-sm" id="username" name="username">
  </div>
  <div class="form-group row small">
    <label for="password">Пароль</label>
    <input type="password" class="form-control form-control-sm" id="password" name="password">
  </div>
  <button type="submit" class="btn btn-outline-primary btn-sm">Применить</button>
</form>

</div>

%include tpls/footer

