<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  import QuestionCreate from "./routes/QuestionCreate.svelte"
  import Navigation from "./components/Navigation.svelte"

  const routes = { // URL 규칙
    '/': Home,
    '/detail/:question_id': Detail,
    '/question-create': QuestionCreate,
  }
</script>

<Navigation />
<Router {routes}/>
