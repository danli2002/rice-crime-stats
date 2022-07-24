import React, { Fragment, useState, useEffect } from 'react'
import { getData } from '../features/data'



export const Home: React.FC = () => {
  const [getMessage, setGetMessage] = useState()

  useEffect(()=>{
    getData().then(response => setGetMessage(response.message))
  }, [])

  console.log(getMessage);

  return (
    <Fragment>
      <h1>Hello!</h1>
      <div>{getMessage ?

      <p>
        {getMessage}
      </p>
      :
      <p>
        Loading
      </p>
      }
      </div>
    </Fragment>
  )
}
