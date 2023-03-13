import Navbar from './Navbar';
import Banner from './Banner';
import classes from './Dashboard.module.css';
import ContentSlider from './ContentSlider';
const Dashboard = () => {
    return (<>
        <div className={classes["background-container"]}>
            <img className={classes.moon} src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/1231630/moon2.png" alt="" />
            <div className={classes.stars}></div>
            <div className={classes.twinkling}></div>
            <div className={classes.clouds}></div></div>
        <Navbar />
        <Banner />
        <ContentSlider />
    </>)
}
export default Dashboard;