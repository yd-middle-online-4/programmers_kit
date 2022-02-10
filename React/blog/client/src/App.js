import React, { Component } from 'react';
import Customer from './components/Customer'
import './App.css';
import { Table } from '@material-ui/core';
import { Paper } from '@material-ui/core';
import { TableHead } from '@material-ui/core/';
import { TableBody } from '@material-ui/core/';
import { TableRow } from '@material-ui/core';
import { TableCell } from '@material-ui/core';
import { withStyles } from '@material-ui/styles';

const styles = theme => ({
  root: {
    width: '100%',
    overflowX: "auto"
  },
  table: {
    minWidth: 1080
  }
})

const customers = [
  {
  'id': '1',
  'image': 'https://placeimg.com/64/64/1',
  'name': '강민승',
  'birthday': '960615',
  'gender': '남자',
  'job': '음악 프로듀서'
  },
  {
  'id': '2',
  'image': 'https://placeimg.com/64/64/2',
  'name': '최선후',
  'birthday': '960314',
  'gender': '남자',
  'job': '대학생'
  },
  {
  'id': '3',
  'image': 'https://placeimg.com/64/64/3',
  'name': '김도경',
  'birthday': '960930',
  'gender': '남자',
  'job': '음악 프로듀서'
  }
]
class App extends Component {
  render() {
    const { classes } = this.props;
    return (
        <Paper className={classes.root}>
          <Table className={classes.table}>
            <TableHead>
              <TableRow>
                <TableCell>번호</TableCell>
                <TableCell>사진</TableCell>
                <TableCell>이름</TableCell>
                <TableCell>생년월일</TableCell>
                <TableCell>성별</TableCell>
                <TableCell>직업</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {customers.map(c => {return (<Customer key={c.id} id={c.id} image={c.image} name={c.name} birthday={c.birthday} gender={c.gender} job={c.job}></Customer>)})}
            </TableBody>
          </Table>
        </Paper>
      );
    }
  }

export default withStyles(styles)(App);
