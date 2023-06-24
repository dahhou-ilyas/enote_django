import './App.css';
import Header from './components/Header';
import NoteListePge from './pages/NoteListePge';
import {
  BrowserRouter as Router,
  Route,
  Routes

} from "react-router-dom";
import NotePage from './pages/NotePage';





function App() {
  return (
    <Router>

      <div className='container'>
        <div className='app'>
          <Header/>
          <Routes>
            <Route exact path="/" element={<NoteListePge/>} />
            <Route path='/note/:id' Component={NotePage} />

          </Routes>

        </div>
      </div>
    </Router>
  );
}

export default App;
