import React, { useState } from 'react'
import Users from '../Data/Username.json';
import  { Navigate } from 'react-router-dom'
import './LoginPage.css';
import './Button.css'
const LoginPage = () => {
  const[username,ChangeUsername] = useState("");
  const[Password,ChangePassword] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  
  const UsernameEntered = (e)=>{
    let Username = e.target.value;
    ChangeUsername(Username);
  }
  const PasswordEntered = (e)=>{
    let Password = e.target.value;
    ChangePassword(Password);
  }

  const CheckCredentials = () => {
    const UsersList = Users.Users;
    for(let i = 0 ; i < UsersList.length ; i++){
      let element = UsersList[i];
      if(username === element.username && Password === element.password){
        setIsLoggedIn(true);
        break;
      }
    }    
  }
  return (
    <>
    {isLoggedIn && <Navigate to='/dashboard' />}
    <div className='Container h-screen w-screen flex justify-center items-center'>
      <div className='WrapperClass bg-[color:#722F37] h-[500px] w-[400px] rounded-lg border-4 border-cyan-950' >
        <div className='flex flex-col gap-2 pl-2'>
            <label className='pl-5 text-xl font-bold text-[color:#BEDF7C]'>Username : </label>   
            <input className='w-[50%] rounded-sm pl-2 border-2 border-black' type="text" placeholder="Enter Username" name="username" required onChange={UsernameEntered} />
            <label className='pl-5 text-xl font-bold text-[color:#BEDF7C]'>Password : </label>
            <input className='w-[50%] rounded-sm pl-2 border-2 border-black' type="password" placeholder="Enter Password" name="password" required onChange={PasswordEntered} />            
            <button className='ml-12 mt-16' onClick={()=>CheckCredentials()}>
              <a href="#" class="button button--pen">
              <div class="button__wrapper">
                <span class="button__text">Welcome</span>
              </div>
              <div class="characterBox">
                <div class="character wakeup">
                <div class="character__face"></div>
                <div class="charactor__face2"></div>
              </div>
              <div class="character wakeup">
                <div class="character__face"></div>
                <div class="charactor__face2"></div>
              </div>
              <div class="character">
                <div class="character__face"></div>
                <div class="charactor__face2"></div>
            </div>
        </div>
    </a>
</button>
        </div>
      </div>
    </div>
    </>
  )
}

export default LoginPage;