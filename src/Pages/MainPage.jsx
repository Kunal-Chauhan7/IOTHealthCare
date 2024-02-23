import React from 'react'
import MyComponent1 from '../Components/MyComponent1';
import MyComponent2 from '../Components/MyComponent2';
import MyComponent3 from '../Components/MyComponent3';
import MyComponent4 from '../Components/MyComponent4';
import MyComponent5 from '../Components/MyComponent5';
import MyComponent6 from '../Components/MyComponent6';

const MainPage = () => {
  return (
    <>
    <div className='bg-gradient-to-r from-rose-100 to-teal-100'>
      <div className='name flex justify-center font-bold text-rose-400'>
        <h3>Medical Info</h3>
      </div>
      <div className='name flex justify-center font-semibold text-blue-500'>
        <h4>Ryan Ghosling</h4>
      </div >
      <div className='name flex justify-center font-semibold text-blue-500'>
        <a href="http://192.168.86.174/html/index.php">Patient Live View</a>
      </div>
      <div className='grid grid-cols-2 gap-4'>
        <MyComponent1/>
        <MyComponent2/>
        <MyComponent3/>
        <MyComponent4/>
        <MyComponent5/>
        <MyComponent6/>
      </div>
    </div>

    </>
  )
}

export default MainPage;