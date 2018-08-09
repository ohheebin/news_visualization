<%@page contentType="text/html; charset=UTF-8" %>
<%@ page import = "java.sql.*" %>    
<%
//키워드 체크 jsp
request.setCharacterEncoding("UTF-8");
String Keyword= request.getParameter("keyword");
String userSearch="";
String db_url = "jdbc:mysql://localhost:3306/news";
String db_id = "root";
String db_pw = "140508";

   Connection conn = null;
   PreparedStatement pstmt = null;
   Statement stmt = null;
   String Query ="";


ResultSet rs = null;

try{
		Class.forName("com.mysql.jdbc.Driver"); 

		conn = DriverManager.getConnection(db_url, db_id, db_pw);
		
		Query = "select noun from word2vec where noun= '"+Keyword+"'" ;
		stmt = conn.createStatement();

		rs = stmt.executeQuery(Query);

		while (rs.next()) {
				//테이블에 저장된 애트리뷰트 이름
				userSearch = rs.getString("noun");
		}
		if(Keyword == ""){
			%>
			<script>
				alert("키워드를 입력하십시오.");
				window.location = "home2.jsp";
			</script>
			<%
		}
		else if((userSearch.equals(Keyword))) 
		{
				session.setAttribute("S_noun", userSearch);
				session.setMaxInactiveInterval(1000);
				response.sendRedirect("./main2.jsp");
		}else{
            %>
			<script>
			alert("입력한 키워드가 존재하지 않습니다.");
			window.location = "home2.jsp";
			</script>
			<%
        }
}catch(Exception e){
}finally{
		if (rs!= null) {
				rs.close();
		}  
		if (pstmt!= null) {
				pstmt.close();
		}

		if (conn!= null) {
				conn.close();
		}

}

%>
