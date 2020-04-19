export default function (context){
    const authenticated = context.store.getters['agents/isAuthenticated'];
    // console.log("[Middleware] : Authentication. User authenticated: ", authenticated  )    

    if (!authenticated){
        context.redirect("/login")
    }
}