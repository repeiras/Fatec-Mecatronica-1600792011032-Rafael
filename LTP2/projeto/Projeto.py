<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>SORTEIO DE TIMES DE FUTSAL</title>
  </head>
  <body style="background-color:yellow;">
    <div class="container">
        <div class="page-header">
            <h1 style = "color:black;" align = "center">SORTEIO DE 3 TIMES DE FUTSAL</h1>
        </div>
        <img src="{{ url_for('static', filename='futsal-jec.jpg') }}"height="30%" width="50%">
        <table class="table table-striped table-responsive table-bordered">
            <thead class="thead-default">
                <tr>
                     <h2>Insira o nome dos jogadores</h2>
                </tr>
                <tr>
                    <th>TIMES:</th>
                </tr>
                <tr>
                     </br><input type = "text"></br>
                      <input type = "text"></br>
                       <input type = "text"></br>
                        <input type = "text"></br>
                          <input type = "text"></br>
                           <input type = "text"></br>
                           <input type = "text"></br>
                           <input type = "text"></br>
                           <input type = "text"></br>
                           <input type = "text"></br>
                           <input type = "text"></br>
                           <input type = "text"></br>
                           <input type = "text"></br>
                           <input type = "text"></br>
                           <input type = "text"></br>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Time1</td>
                </tr>
                <tr>
                    <td>------</td>
                </tr>
                <tr>
                    <td>Time2</td>
                </tr>
                <tr>
                    <td>------</td>
                </tr>
                <tr>
                    <td>Time3</td>
                </tr>
                <td>------</td>
                <tr>
                    <td>Valor total da quadra:</td>
                </tr>
                <tr>
                    <td>------</td>
                </tr>
                <tr>
                    <td>Valor da quadra para cada jogador:</td>
                </tr>
                <tr>
                    <td>------</td>
                </tr>
            </tbody>
        </table>
    </div>
  </body>
</html>
