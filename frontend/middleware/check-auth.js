export default function(context) {
  console.log("[Middleware]: Initiating check auth");
  context.store.dispatch("agents/initAuth", context.req);
}
