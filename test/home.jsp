<%@page contentType="text/html; charset=UTF-8" %>
<%@ page import = "java.sql.*" %>
<!DOCTYPE html>
<html>
<head>
        <meta charset="UTF-8">
        <title>홈 화면</title>
        <link rel="stylesheet" type="text/css" href="stylesheet.css">
</head>

<body>
        <header>
                <div id="upper">
                        <h1>News Visualization</h1>
                </div>
        </header>
        <aside id="login">
                <table id="table">
                        <form method="post" action="keyword_check.jsp">
                        <tr>
                        <td>
                                search :<input type="text" id="keyword" name="keyword"></input>
                        </td>
                        <td>
                        <input type="submit" value="검색" id="button">
                        </form>
                        </td>
                        </tr>
                </table>
        </aside>
        <script type="text/javascript" src="myScript.js"></script>
</body>
</html>