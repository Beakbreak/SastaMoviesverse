
import Banner from './Banner';
import Navmenu from './Navmenu';
import classes from './Dashboard.module.css';
import ContentSlider from './ContentSlider';
const Dashboard = () => {
    return (<>
        <div className={classes["background-container"]}>
            <img className={classes.moon} src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/1231630/moon2.png" alt="" />
            <div className={classes.stars}></div>
            <div className={classes.twinkling}></div>
            <div className={classes.clouds}></div></div>
        <Navmenu />
        <Banner />


        <ContentSlider title="Suggested For You" />
        <ContentSlider title="Most Rated" />
        <ContentSlider title="Trending" />
        <ContentSlider title="Action Movies" />
        <ContentSlider title="Adventure Movies" />
        <ContentSlider title="War Movies" />
        <ContentSlider title="Fantasy Movies" />
        <ContentSlider title="Horror Movies" />
        <ContentSlider title="Documentary Movies" />
        <ContentSlider title="Mystery Movies" />
        <ContentSlider title="Drama Movies" />
        <ContentSlider title="Kids' Movies" />
        <ContentSlider title="Romance Movies" />
        <ContentSlider title="IMAX Movies" />
        <ContentSlider title="Comedy Movies" />
        <ContentSlider title="Western Movies" />
        <ContentSlider title="Animation Movies" />
        <ContentSlider title="Crime Movies" />
        <ContentSlider title="Musical Movies" />
        <ContentSlider title="Thriller Movies" />
        <ContentSlider title="Sci-Fi Movies" />
        <ContentSlider title="Film Noir Movies" />
    </>)
}
export default Dashboard;