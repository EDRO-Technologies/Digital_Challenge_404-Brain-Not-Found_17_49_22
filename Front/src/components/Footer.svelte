<script>
	import { text } from "@sveltejs/kit";

  export let isMainPage = "false";
</script>

<footer>
  <style>
    .footer {
      height: 50px;
      background-color: #333;
      color: white;
      text-align: center;
      left: 0;
      bottom: 0;
      width: 100%; 
      z-index: 2;
      display: flex;
      justify-content: center;
      margin-top:10px
    }
  
    .copyright {
      margin-top: 15px;
      font-size: 14px;
    }
  </style>
  
  <footer class="footer" style={isMainPage == "true" ? "position: fixed" : ""}>
    <div class="copyright">
      © 2024 Мозгов нет. Права защищать не будем.
    </div>
  </footer>
</footer>