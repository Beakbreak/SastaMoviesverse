import classes from "./MoviePoster.module.css";
const MoviePoster = props => {
    return (<>
        <div className={classes.imgcontainer}><img className={classes.posterimg} src={`http://image.tmdb.org/t/p/w500/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg`} /></div></>);
}

export default MoviePoster;