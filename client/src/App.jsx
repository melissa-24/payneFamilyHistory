import {Routes, Route} from 'react-router-dom'


// Base imports
import Header from './components/base/Header'
import Footer from './components/base/Footer'

// Routes
import Home from './views/Home'

function App() {


  return (
    <>
      <Header />
      <main>
        <Routes>
          <Route exact path="/" element={<Home />} />
        </Routes>
      </main>
      <Footer />
    </>
  )
}

export default App