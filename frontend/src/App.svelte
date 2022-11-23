<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"

  const routes = { // URL 규칙
    '/': Home,
    '/detail/:question_id': Detail,
  }
</script>

<Router {routes}/>
