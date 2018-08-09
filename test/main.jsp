<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8" %>

<%@ page import = "java.sql.*" %>

<%
request.setCharacterEncoding("UTF-8");
String nouns = (String)session.getAttribute("S_noun");
Connection conn = null;                                        // null로 초기화 한다.
PreparedStatement pstmt = null;
Statement stmt = null;
ResultSet rs = null;
String search_noun = "";
String synonyms1 = "";
String synonyms2 = "";
String synonyms3 = "";
String synonyms4 = "";
String synonyms5 = "";
try{

        String user_url = "jdbc:mysql://localhost:3306/news";
        String id = "root";
        String pw = "140508";
        

        Class.forName("com.mysql.jdbc.Driver");
        conn=DriverManager.getConnection(user_url,id,pw);

        stmt = conn.createStatement();
        String query = "select noun, synonyms_1, synonyms_2, synonyms_3, synonyms_4, synonyms_5 from word2vec where noun=\"";
        query += nouns;
        query += "\"";
        rs = stmt.executeQuery(query);

        while(rs.next()){
            search_noun = rs.getString("noun");
            synonyms1 = rs.getString("synonyms_1");
            synonyms2 = rs.getString("synonyms_2");
            synonyms3 = rs.getString("synonyms_3");
            synonyms4 = rs.getString("synonyms_4");
            synonyms5 = rs.getString("synonyms_5");
        }
%>
<!DOCTYPE html>
<html>
    <title>메인 화면</title>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="mainStyle.css"/>
    </head>
</head>
<body>
     <div id="container">
         <div id="header">
            <a id="title" onclick="gohome()">News Visualization</a>
         </div>
         <div id="content">
            <div class="circle-text" onclick="news_search('news_data','news_data1','news_data2','news_data3','news_data4','news_data5')" style="left: 600px; top: 300px;">
                <%=search_noun%>
            </div>
            <div class="circle-text" onclick="news_search('news_data1','news_data','news_data2','news_data3','news_data4','news_data5')" style="left: 350px; top: 170px;">
                <%=synonyms1%>
            </div>
            <div class="circle-text" onclick="news_search('news_data2','news_data1','news_data','news_data3','news_data4','news_data5')" style="left: 500px; top: 100px;">
                <%=synonyms2%>
            </div>
            <div class="circle-text" onclick="news_search('news_data3','news_data1','news_data2','news_data','news_data4','news_data5')" style="left: 600px; top: 300px;">
                <%=synonyms3%>
            </div>
            <div class="circle-text" onclick="news_search('news_data4','news_data1','news_data2','news_data3','news_data','news_data5')" style="left: 10px; top: 530px;">
                <%=synonyms4%>
            </div>
            <div class="circle-text" onclick="news_search('news_data5','news_data1','news_data2','news_data3','news_data4','news_data')" style="left: 400px; top: 600px;">
                <%=synonyms5%>
            </div>
            <svg height="600" width="1100">
                <line x1="650" y1="250" x2="470" y2="100" id="line"/>
                <line x1="650" y1="250" x2="740" y2="50" id="line"/>
                <line x1="650" y1="250" x2="950" y2="250" id="line"/>
                <line x1="650" y1="250" x2="450" y2="500" id="line"/>
                <line x1="650" y1="250" x2="950" y2="550" id="line"/>
            </svg>
            <%
        }catch(Exception e){
            e.printStackTrace();
        }
        %>
         </div>
         <div id="sideinfo">
               <div id="synonyms">
                    
                        <form method="post" action="keyword_check.jsp">
                            <tr>
                                <td>
                                    <input type="text" id="main_search" value="<%=nouns%>" name="keyword"/>
                                </td>
                                <td>
                                    <input type="submit" value="검색" class="btn-2">
                                </td>
                            </tr>
                        </form>
                </div>
                <div id="news_data">
            <%
            try{
                String user_url = "jdbc:mysql://localhost:3306/news";
                String id = "root";
                String pw = "140508";
                
                Class.forName("com.mysql.jdbc.Driver");
                conn=DriverManager.getConnection(user_url,id,pw);

                stmt = conn.createStatement();
                String query = "select * from data where title Like '%"+search_noun+"%';";
                rs = stmt.executeQuery(query);

                while(rs.next()){
                    %>
                    <a href="<%=rs.getString("url")%>" target="_blank" id="news"><%=rs.getString("title")%></a><br>
                    <%
                }
             
            }catch(Exception e){
                e.printStackTrace();
            }
            %>
                </div>
                <div id="news_data1" style= "display: none;">
                    <%
            try{
                String user_url = "jdbc:mysql://localhost:3306/news";
                String id = "root";
                String pw = "140508";
                
                Class.forName("com.mysql.jdbc.Driver");
                conn=DriverManager.getConnection(user_url,id,pw);

                stmt = conn.createStatement();
                String query = "select * from data where title Like '%"+synonyms1+"%';";
                rs = stmt.executeQuery(query);


                while(rs.next()){
                    %>
                    <a href="<%=rs.getString("url")%>" target="_blank" id="news"><%=rs.getString("title")%></a><br>
                    <%
                }
             
            }catch(Exception e){
                e.printStackTrace();
            }
            %>
            </div>
            <div id="news_data2" style= "display: none;">
                    <%
            try{
                String user_url = "jdbc:mysql://localhost:3306/news";
                String id = "root";
                String pw = "140508";
                
                Class.forName("com.mysql.jdbc.Driver");
                conn=DriverManager.getConnection(user_url,id,pw);

                stmt = conn.createStatement();
                String query = "select * from data where title Like '%"+synonyms2+"%';";
                rs = stmt.executeQuery(query);


                while(rs.next()){
                    %>
                    <a href="<%=rs.getString("url")%>" target="_blank" id="news"><%=rs.getString("title")%></a><br>
                    <%
                }
             
            }catch(Exception e){
                e.printStackTrace();
            }
            %>
            </div>
            <div id="news_data3" style= "display: none;">
                    <%
            try{
                String user_url = "jdbc:mysql://localhost:3306/news";
                String id = "root";
                String pw = "140508";
                
                Class.forName("com.mysql.jdbc.Driver");
                conn=DriverManager.getConnection(user_url,id,pw);

                stmt = conn.createStatement();
                String query = "select * from data where title Like '%"+synonyms3+"%';";
                rs = stmt.executeQuery(query);


                while(rs.next()){
                    %>
                    <a href="<%=rs.getString("url")%>" target="_blank" id="news"><%=rs.getString("title")%></a><br>
                    <%
                }
             
            }catch(Exception e){
                e.printStackTrace();
            }
            %>
            </div>
            <div id="news_data4" style= "display: none;">
                    <%
            try{
                String user_url = "jdbc:mysql://localhost:3306/news";
                String id = "root";
                String pw = "140508";
                
                Class.forName("com.mysql.jdbc.Driver");
                conn=DriverManager.getConnection(user_url,id,pw);

                stmt = conn.createStatement();
                String query = "select * from data where title Like '%"+synonyms4+"%';";
                rs = stmt.executeQuery(query);


                while(rs.next()){
                    %>
                    <a href="<%=rs.getString("url")%>" target="_blank" id="news"><%=rs.getString("title")%></a><br>
                    <%
                }
             
            }catch(Exception e){
                e.printStackTrace();
            }
            %>
            </div>
            <div id="news_data5" style= "display: none;">
                    <%
            try{
                String user_url = "jdbc:mysql://localhost:3306/news";
                String id = "root";
                String pw = "140508";
                
                Class.forName("com.mysql.jdbc.Driver");
                conn=DriverManager.getConnection(user_url,id,pw);

                stmt = conn.createStatement();
                String query = "select * from data where title Like '%"+synonyms5+"%';";
                rs = stmt.executeQuery(query);


                while(rs.next()){
                    %>
                    <a href="<%=rs.getString("url")%>" target="_blank" id="news"><%=rs.getString("title")%></a><br>
                    <%
                }
             
            }catch(Exception e){
                e.printStackTrace();
            }
            %>
            </div>
         </div>
         <div id="footer"></div>
     </div>
     <script type="text/javascript" src="myScript.js"></script>
</body>
</html>