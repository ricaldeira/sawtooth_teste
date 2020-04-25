export default function (context){
    const authenticated = context.store.getters['agents/isAuthenticated'];
    console.log("[Middleware] : Authentication. User authenticated: ", authenticated  )    

    if (!authenticated){
        console.log("[Middleware]: Sending to login")
        context.redirect("/login")
    }
}