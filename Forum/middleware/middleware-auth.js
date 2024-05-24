export default function ({ route, redirect }) {
  // route.name chứa tên của route hiện tại

  if (!localStorage.getItem('accessToken') || !localStorage.getItem('user')) {
    console.log(route)

    // Nếu route là '/auth/login', bạn có thể thực hiện redirect
    if (!route.name.includes('auth') && !route.name.includes('book')) {
      return redirect('/auth/login')
    }
  }
}
